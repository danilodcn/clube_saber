from collections import defaultdict

from django.db.models import QuerySet

from ..models.site import Gradient, GradientSiteTheme, SiteTheme

DEFAULT_GRADIENT_DEG: dict[str, str] = defaultdict(lambda: '90deg')


def list_gradients(theme: SiteTheme):
    all_gradients = get_list_gradients(theme)
    result: dict[str, str] = {}

    for type, gradients in all_gradients.items():
        deg = DEFAULT_GRADIENT_DEG[type]
        colors = ','.join(
            map(lambda x: f'{x.color} {x.percentage}%', gradients)
        )
        result[type] = f'linear-gradient({deg}, {colors})'
    return result


def get_list_gradients(theme: SiteTheme):
    all_gradients = GradientSiteTheme.objects.filter(site_theme=theme)
    primaries = all_gradients.filter(type=GradientSiteTheme.Type.primary)
    primary_gradient = get_ordering_gradients(primaries)

    gradients: dict[GradientSiteTheme.Type, list[Gradient]] = {}

    for type in GradientSiteTheme.Type:
        if type == GradientSiteTheme.Type.primary:
            gradients[type] = primary_gradient

        processed_gradients = get_ordering_gradients(
            gradients=all_gradients.filter(type=type)
        )

        if len(processed_gradients) == 0:
            processed_gradients = primary_gradient

        gradients[type] = processed_gradients

    return gradients


def get_ordering_gradients(gradients: 'QuerySet[GradientSiteTheme]'):
    result: list[Gradient] = []
    gradients_iterator = gradients.order_by('percentage').values_list(
        'color', 'percentage'
    )
    for color, percentage in gradients_iterator:
        result.append(Gradient(color=color, percentage=percentage))

    return result
