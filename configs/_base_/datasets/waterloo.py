import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class WaterlooDataset(CustomDataset):
    """HRF dataset.
    In segmentation map annotation for waterloo, 0 stands for background, which is
    included in 2 categories. ``reduce_zero_label`` is fixed to False. The
    ``img_suffix`` is fixed to '.png' and ``seg_map_suffix`` is fixed to
    '.png'.
    """

    CLASSES = ('background', 'building')

    PALETTE = [[0, 0, 0], [255, 255, 255]]

    def __init__(self, **kwargs):
        super(WaterlooDataset, self).__init__(
            img_suffix='.tif',
            seg_map_suffix='.tif',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)