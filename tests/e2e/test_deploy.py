from e2e.utils import _configure_env, _create_esc, _delete_workload, _deploy_and_verify, _wait_for_components


def test_deploy_model():
    _configure_env()
    _wait_for_components()
    esc = _create_esc()

    # Wipe out older workloads, then send deploy request to Lifecycle
    _delete_workload('adder')
    _deploy_and_verify('sample/python-class', 'adder', esc)
