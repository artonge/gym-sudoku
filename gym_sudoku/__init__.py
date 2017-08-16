from gym.envs.registration import register

register(
    id='Sudoku-v0',
    entry_point='gym_sudoku.envs:SudokuEnv',
    reward_threshold = 40.0,
)
