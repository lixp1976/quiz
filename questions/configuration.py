__author__ = 'djud'


def get_testing_config():
    return {
        'timeout': 60 * 20, # 20 min
        'marks': [
            {
                'mark': 2,
                'min_answers': 1,
            },

            {
                'mark': 3,
                'min_answers': 2,
            },

            {
                'mark': 4,
                'min_answers': 3,
            }
        ]


    }


def update_testing_config():
    pass