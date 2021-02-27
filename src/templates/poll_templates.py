from src.queries.session_handlers import handle_session


def create_letters_poll(card_class, Session, engine) -> dict:
    letters = [handle_session(card_class().get_random,
                              Session,
                              engine
                              )for _ in range(4)]

    return {number: letter for number, letter in enumerate(letters)}


def create_poll_template(poll_data: dict) -> str:
    return "\n"+"\n".join(
        [f"{n}. {letter}" for n, letter in poll_data.items()])
