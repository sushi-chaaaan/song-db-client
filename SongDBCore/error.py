import traceback


class DBAccessError(Exception):
    def __init__(self, **kwargs: object) -> None:
        super().__init__()
        traceback.print_exc()
        print(**kwargs)
        pass
