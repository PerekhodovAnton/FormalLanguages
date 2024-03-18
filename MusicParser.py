from lark import Lark

# Определение грамматики
music_grammar = """
    start: music_piece+

    music_piece: phrase+

    phrase: note
          | chord
          | rest

    note: PITCH DURATION?
    chord: "[" note+ "]"
    rest: "rest" DURATION

    PITCH: /[A-G][#]?/
    DURATION: /[1-9][0-9]*/

    %import common.WS
    %ignore WS
"""

# Функция для разбора текста с использованием грамматики
def parse_music(text):
    parser = Lark(music_grammar, start='start')
    try:
        return parser.parse(text)
    except Exception as e:
        print("Ошибка при разборе:", e)

# Функция для разделения нот и длительностей
def split_notes_and_durations(text):
    parts = text.split()
    note_parts = []
    duration_parts = []
    for part in parts:
        if part.isdigit():
            duration_parts.append(part)
        else:
            # Нужно проверить, если предыдущий элемент был числом
            if duration_parts and duration_parts[-1] == note_parts[-1]:
                duration_parts[-1] += part
            else:
                note_parts.append(part)
    return note_parts, duration_parts


# Пример использования
music_text = "A4 B4 4 C4 2"
notes, durations = split_notes_and_durations(music_text)
parsed_music = parse_music(" ".join(notes))
if parsed_music:
    print("Разбор успешен!")
# Дерево
print(parsed_music)
