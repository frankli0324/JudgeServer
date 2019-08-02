from _judger import (
    RESULT_SUCCESS, RESULT_CPU_TIME_LIMIT_EXCEEDED,
    RESULT_MEMORY_LIMIT_EXCEEDED,
    RESULT_REAL_TIME_LIMIT_EXCEEDED,
    RESULT_RUNTIME_ERROR, RESULT_SYSTEM_ERROR,
    RESULT_WRONG_ANSWER
)

RESULT_PRESENTATION_ERROR = -2
RESULT_COMPILE_ERROR = 6
result_msg = {
    RESULT_SUCCESS: 'Accepted',
    RESULT_RUNTIME_ERROR: 'Runtime Error',
    RESULT_WRONG_ANSWER: 'Wrong Answer',
    RESULT_CPU_TIME_LIMIT_EXCEEDED: 'Time Limit Exceeded',
    RESULT_REAL_TIME_LIMIT_EXCEEDED: 'Time Limit Exceeded',
    RESULT_SYSTEM_ERROR: 'System Error',
    RESULT_MEMORY_LIMIT_EXCEEDED: 'Memory Limit Exceeded',
    RESULT_PRESENTATION_ERROR: 'Presentation Error',
    RESULT_COMPILE_ERROR: 'Compile Error'
}