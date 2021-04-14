class StudentProfile:
    """
    Class Handling StudentProfile.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes StudentProfile object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """
        self.email = kwargs.get('email', "")
        self.name = kwargs.get('name', "")
        self.year = kwargs.get('year', "")
        self.batch = kwargs.get('batch', "")
        self.enrolledSubjects = kwargs.get('enrolledSubjects', [])
        self.prn = kwargs.get('prn', "")


class TeacherProfile:
    """
    Class Handling TeacherProfile.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes TeacherProfile object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """
        self.email = kwargs.get('email', "")
        self.name = kwargs.get('name', "")
        self.department = kwargs.get('department', "")
        self.enrolledSubjects = kwargs.get('enrolledSubjects', [])
        self.prn = kwargs.get('prn', "")


class Lecture:
    """
    Class Handling LectureCalender.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes LectureCalender object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """
        self.lecture_id = kwargs.get('lecture_id', "")
        self.subject_id = kwargs.get('subject_id', "")
        self.lecture_day = kwargs.get('lecture_day', "0")
        self.lecture_time = kwargs.get('lecture_time', "0")
        self.attention_data = kwargs.get('attention_data', [])
        self.quiz_data = kwargs.get('quiz_data', [])


class Subject:
    """
    Class Handling Subjects.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes Subject object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """

        self.subject_id = kwargs.get('subject_id', "")
        self.teacher_email = kwargs.get('teacher_email', "")
        self.total_lectures = kwargs.get('total_lectures', "")
