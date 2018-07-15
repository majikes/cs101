from django.db import models

class Question(models.Model):
    """ Question shown to the student """
    description = models.TextField(null=False,
                                   blank=False,
                                   help_text="Description of the question shown to the student.")
    code_pre_statements = models.TextField(null=True,
                                           blank=True,
                                           help_text="Python statements prior to the student answer area.")
    code_post_statements = models.TextField(null=True,
                                            blank=True,
                                            help_text="Python statements after the student answer area.")

class Answer(models.Model):
    """ Answer entered by the student """
    question = models.ForeignKey(Question)
    answer_statements = models.TextField(null=False,
                                         blank=False,
                                         help_text="Answer submitted to the question.")

