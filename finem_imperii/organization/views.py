from django.shortcuts import render, get_object_or_404

from decorators import inchar_required
from organization.models import Organization


@inchar_required
def organization_view(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    context = {
        'organization': organization,
        'hero_is_member': organization.character_is_member(request.hero),
    }
    return render(request, 'organization/view_organization.html', context)


@inchar_required
def documents_view(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    context = {
        'organization': organization,
        'hero_is_member': organization.character_is_member(request.hero),
    }
    return render(request, 'organization/view_documents.html', context)