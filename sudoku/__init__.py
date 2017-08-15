import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Sudoku-v0',
    entry_point='sudoku.envs:SudokuEnv',
    reward_threshold = 40,
    nondeterministic = False,
)
