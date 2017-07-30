from xml.etree import ElementTree
import os
import collections

Course = collections.namedtuple('Course', 'title room building')


def main():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    dom = ElementTree.fromstring(xml_text)

    course_nodes = dom.findall('course')

    courses = []

    for n in course_nodes:
        c = Course(

            n.find('title').text,
            n.find('place/room').text,
            n.find('place/building').text
        )
        courses.append(c)

    input_building = input('Enter building: ')
    input_room = input('Enter room number: ')

    room_courses = [
        c.title
        for c in courses
        if c.building == input_building and c.room == input_room
            ]

    for c in room_courses:
        print(c)


if __name__ == '__main__':
    main()


