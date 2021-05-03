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
        self.prn = kwargs.get('prn', "")
        self.role = kwargs.get('role', "")


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
        self.prn = kwargs.get('prn', "")
        self.role = kwargs.get('role', "")


class Lecture:
    """
    Class Handling Lecture.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes Lecture object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """
        self.lecture_id = kwargs.get('lecture_id', "")
        self.subject_id = kwargs.get('subject_id', "")
        self.lecture_day = kwargs.get('lecture_day', "0")
        self.lecture_time = kwargs.get('lecture_time', "0")
        self.teacher_id = kwargs.get('teacher_id', "")
        # self.attention_data = kwargs.get('attention_data', [])


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
        self.email = kwargs.get('email', "")
        self.total_lectures = kwargs.get('total_lectures', "")


class QuizData:
    """
    Class Handling Subjects.
    """

    def __init__(self, **kwargs):
        """
        Method which initializes Subject object

        Args -

            kwargs: key word arguments containing initialization information for the object
        """
        self.quiz_id = kwargs.get('quiz_id', "")
        self.question = kwargs.get('question', "")
        self.option_one = kwargs.get('option_one', "")
        self.option_two = kwargs.get('option_two', "")
        self.option_three = kwargs.get('option_three', "")
        self.option_four = kwargs.get('option_four', "")
        self.correct_option = kwargs.get('correct_option', "")
        self.solution = kwargs.get('solution', "")
        self.lecture_id = kwargs.get('lecture_id', "")
        self.subject_id = kwargs.get('subject_id', "")
        self.quiz_data = kwargs.get('quiz_data', [])
