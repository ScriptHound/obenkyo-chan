from typing import Any, Callable


def handle_session(query: Callable, session_cls, engine, *args) -> Any:
    conn = engine.connect()
    session = session_cls(bind=conn)
    result = None

    try:
        result = query(*args, session=session)
        session.expunge_all()

        session.commit()

    except Exception:
        session.rollback()
        raise RuntimeError('Query failed')

    finally:
        session.close()

    return result
