from gym.envs.registration import register

register(
    id='Sudoku-v0',
    entry_point='envs:SudokuEnv',
    reward_threshold = 40,
    nondeterministic = False,
)
