import sys
from tasks import (
    generate_reply_spider_task,
    get_dynamic_base_data_task
)


def init_dynamic():
    asoul_member_ids = [672346917, 672342685, 672353429, 351609538, 672328094]
    get_dynamic_base_data_task.delay(asoul_member_ids, 5)


def init_reply():
    generate_reply_spider_task.delay(True)


if __name__ == '__main__':
    if len(sys.argv) >= 1:
        if sys.argv[1] == 'init_reply':
            init_reply()
        elif sys.argv[1] == 'init_dynamic':
            init_dynamic()
        elif sys.argv[1] == 'register_scheduler':
            # TODO: register schedulers after init dynamic and reply
            pass
