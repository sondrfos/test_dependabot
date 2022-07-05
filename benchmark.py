import time

import pytest


@pytest.mark.benchmark(
    group="x20",
    timer=time.time,
)
def test_clustering_performance_cluster_every_frame(benchmark):
    @benchmark
    # Code to be measured
    def measure_code():
        time.sleep(5)

    # Extra code, to verify that the run
    # completed correctly.
    # Note: this code is not measured.
    assert measure_code is None
