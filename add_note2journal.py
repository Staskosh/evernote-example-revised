#!/usr/bin/env python
import textwrap
from datetime import date, datetime, timedelta
import argparse

from evernote.api.client import EvernoteClient
from config import Settings


WEEK_DAYS = {
    1: u'понедельник',
    2: u'вторник',
    3: u'среда',
    4: u'четверг',
    5: u'пятница',
    6: u'суббота',
    7: u'воскресенье',
}


def is_valid_date(text):
    text = text.strip()
    if text.startswith('-') or text.startswith('+') or text.isdigit():
        return date.today() + timedelta(days=int(text))
    try:

        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(text)
        raise argparse.ArgumentTypeError(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=u'Adds note to notebook "Дневник", uses template note'
    )
    parser.add_argument('date',
                        nargs='?',
                        type=is_valid_date,
                        help='date in format "YYYY-MM-DD"')
    args = parser.parse_args()

    config = Settings()

    client = EvernoteClient(
        token=config.EVERNOTE_PERSONAL_TOKEN,
        sandbox=True
    )
    noteStore = client.get_note_store()

    day = args.date or date.today()
    context = {
        'date': day.isoformat(),
        'dow': WEEK_DAYS[day.isoweekday()],
    }
    print(textwrap.dedent(
        f'''
        Title Context is:
        {context}'''
    ))

    template_note_guid = config.JOURNAL_TEMPLATE_NOTE_GUID
    notebook_guid = config.JOURNAL_NOTEBOOK_GUID
    new_note = noteStore.copyNote(template_note_guid, notebook_guid)
    new_title = f'{new_note.title} {context["date"]}, {context["dow"]}'
    new_note.title = new_title
    noteStore.updateNote(new_note)

    print(textwrap.dedent(
        f'''
        Note created: {new_title}
        Done'''
    ))
