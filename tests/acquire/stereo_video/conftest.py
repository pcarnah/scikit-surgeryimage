import pytest
from sksurgeryimage.acquire import stereo_video as sv


@pytest.fixture(scope="function")
def interlaced_video_source():
    return sv.StereoVideo(sv.StereoVideoLayouts.INTERLACED,
                          ["tests/output/test-16x8-rgb.avi"])


@pytest.fixture(scope="function")
def vertically_stacked_video_source():
    return sv.StereoVideo(sv.StereoVideoLayouts.VERTICAL,
                          ["tests/output/test-16x8-rgb.avi"])
