import numpy as np
from gymnasium.envs.registration import register



job_machine_matrix = np.array([
    [1, 30, 5],
    [1, 25, 10],
    [2, 40, 5],
    [3, 45, 11],
    [2, 10, 8]
])

jobs = np.array(
    [29, 13, 1, 5, 7]
)

stages_machines = [4, 3, 7]

register(
     id="MyCustomEnv-v0",
     entry_point = "my_custom_env.envs:OperatingRoomScheduling", kwargs={'job_machine_matrix': job_machine_matrix, 'jobs': jobs, 'stages_machines': stages_machines},
)

