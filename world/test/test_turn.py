from django.test import TestCase
from django.urls.base import reverse

from battle.models import Battle
from organization.models import Organization
from world.admin import pass_turn
from world.initialization import initialize_unit, initialize_settlement
from world.models import Tile, WorldUnit, World, TileEvent, Settlement
from world.turn import organizations_with_battle_ready_units, \
    battle_ready_units_in_tile, \
    opponents_in_organization_list, get_largest_conflict_in_list, \
    create_battle_from_conflict, TurnProcessor, do_settlement_barbarian_generation


class TestEmortuusTurn(TestCase):
    fixtures = ['world1']

    def test_pass_one_year_in_emortuus(self):
        for i in range(12):
            pass_turn(None, None, World.objects.all())


class TestTurn(TestCase):
    fixtures = ['simple_world']

    def test_pass_turn_admin_action(self):
        pass_turn(None, None, World.objects.all())

    def test_population_generation_in_empty_settlement(self):
        settlement = Settlement.objects.get(name="Small Fynkah")
        settlement.npc_set.all().delete()
        settlement.update_population()
        self.assertEqual(settlement.population, 0)
        processor = TurnProcessor(settlement.tile.world)
        processor.do_settlement_population_changes(settlement)
        self.assertEqual(settlement.population, 5)

    def test_organizations_with_battle_ready_units(self):
        tile = Tile.objects.get(id=108)
        result = organizations_with_battle_ready_units(tile)
        self.assertIn(Organization.objects.get(id=105), result)
        self.assertIn(Organization.objects.get(id=112), result)
        self.assertEqual(len(result), 2)

    def test_battle_ready_units_in_tile(self):
        tile = Tile.objects.get(id=108)
        result = battle_ready_units_in_tile(tile)
        self.assertIn(WorldUnit.objects.get(id=1), result)
        self.assertIn(WorldUnit.objects.get(id=2), result)
        self.assertEqual(len(result), 3)

    def test_opponents_in_organization_list(self):
        tile = Tile.objects.get(id=108)
        result = opponents_in_organization_list(organizations_with_battle_ready_units(tile), tile)
        self.assertEqual(len(result), 1)
        opponents = result[0]
        self.assertIn(Organization.objects.get(id=105), opponents[0])
        self.assertIn(Organization.objects.get(id=112), opponents[1])
        self.assertEqual(len(opponents), 2)

    def test_get_largest_conflict_in_list(self):
        initialize_unit(WorldUnit.objects.get(id=1))
        initialize_unit(WorldUnit.objects.get(id=2))
        tile = Tile.objects.get(id=108)
        conflicts = opponents_in_organization_list(organizations_with_battle_ready_units(tile), tile)
        result = get_largest_conflict_in_list(conflicts, tile)
        self.assertEqual(len(result), 2)
        self.assertIn(Organization.objects.get(id=105), result[0])
        self.assertIn(Organization.objects.get(id=112), result[1])
        self.assertEqual(len(result), 2)

    def test_create_battle_from_conflict(self):
        initialize_unit(WorldUnit.objects.get(id=1))
        initialize_unit(WorldUnit.objects.get(id=2))
        tile = Tile.objects.get(id=108)
        organization1 = Organization.objects.get(id=105)
        organization2 = Organization.objects.get(id=112)

        battle = create_battle_from_conflict(
            [
                [organization1],
                [organization2]
            ],
            tile
        )
        self.assertEqual(battle.tile, tile)

    def test_create_only_one_conflict(self):
        world = World.objects.get(id=2)
        for unit in WorldUnit.objects.filter(world=world):
            initialize_unit(unit)
        pass_turn(None, None, World.objects.filter(id=2))
        pass_turn(None, None, World.objects.filter(id=2))
        self.assertEqual(Battle.objects.count(), 1)
        Battle.objects.filter(tile__world=world).update(current=False)
        pass_turn(None, None, World.objects.filter(id=2))
        self.assertEqual(Battle.objects.count(), 2)

    def test_world_blocking(self):
        world = World.objects.get(id=2)
        world.blocked_for_turn = True
        world.save()

        self.client.post(
            reverse('account:login'),
            {'username': 'alice', 'password': 'test'},
        )
        response = self.client.get(
            reverse('world:activate_character', kwargs={'char_id': 3}),
            follow=True
        )
        self.assertRedirects(response, reverse('account:home'))

    def test_conquest(self):
        tile = Tile.objects.get(name="More mountains")
        conqueror = Organization.objects.get(id=105)
        tile_event = TileEvent.objects.create(
            tile=tile,
            type=TileEvent.CONQUEST,
            organization=conqueror,
            counter=0,
            start_turn=0
        )
        processor = TurnProcessor(tile.world)
        processor.do_conquests()

        tile.refresh_from_db()
        self.assertNotEqual(tile.controlled_by, conqueror)
        tile_event.refresh_from_db()
        self.assertEqual(tile_event.end_turn, None)
        self.assertEqual(tile_event.counter, 0)

    def test_conquest_end(self):
        tile = Tile.objects.get(id=107)
        conqueror = Organization.objects.get(id=105)
        tile_event = TileEvent.objects.create(
            tile=tile,
            type=TileEvent.CONQUEST,
            organization=conqueror,
            counter=0,
            start_turn=0
        )
        processor = TurnProcessor(tile.world)
        processor.do_conquests()

        tile.refresh_from_db()
        self.assertNotEqual(tile.controlled_by, conqueror)
        tile_event.refresh_from_db()
        self.assertEqual(tile_event.end_turn, 0)
        self.assertNotEqual(tile_event.end_turn, None)

    def test_conquest_success(self):
        tile = Tile.objects.get(name="More mountains")
        conqueror = Organization.objects.get(id=105)
        tile_event = TileEvent.objects.create(
            tile=tile,
            type=TileEvent.CONQUEST,
            organization=conqueror,
            counter=100000,
            start_turn=0
        )
        processor = TurnProcessor(tile.world)
        processor.do_conquests()

        tile.refresh_from_db()
        self.assertEqual(tile.controlled_by, conqueror)
        tile_event.refresh_from_db()
        self.assertEqual(tile_event.end_turn, 0)
        self.assertNotEqual(tile_event.end_turn, None)

    def test_barbarian_non_creation_in_occupied_settlement(self):
        settlement = Settlement.objects.get(name="Small Fynkah")
        initialize_settlement(settlement)

        for unit in settlement.worldunit_set.all():
            initialize_unit(unit)

        do_settlement_barbarian_generation(settlement)
        self.assertFalse(
            settlement.worldunit_set.filter(owner_character__isnull=True).exists()
        )

    def test_barbarian_creation_in_barbaric_settlement(self):
        settlement = Settlement.objects.get(name="Small Shaax")
        initialize_settlement(settlement)

        do_settlement_barbarian_generation(settlement)
        self.assertTrue(
            settlement.worldunit_set.filter(owner_character__isnull=True).exists()
        )
