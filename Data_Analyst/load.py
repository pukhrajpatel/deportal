from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import VillageBoundaryModel

vill_mapping = {
    'state_name':'state_name',
    'ac_no':'ac_no',
    'object_id':'object_id',
    'v_id':'v_id',
    'name':'name',
    'district':'district',
    'subdistric':'subdistric',
    'censusname':'censusname',
    'lgd_villag':'lgd_villag',
    'level_2011':'level_2011',
    'tru_2011':'tru_2011',
    'geometry':'MULTIPOLYGON'
    
}

vill_shp = Path(__file__).resolve().parent / "data" / "village_shape_files.shp"


def run(verbose=True):
    lm = LayerMapping(VillageBoundaryModel, vill_shp, vill_mapping, transform=False)
    lm.save(strict=True, progress=100)