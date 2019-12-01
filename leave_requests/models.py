from django.db import models

from authentication.models import User


class LeaveRequest(models.Model):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    STATUS = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )

    VACATION = 'VACATION'
    SICK = 'SICK'
    MATERNITY = 'MATERNITY'
    UNPAID = 'UNPAID'
    TYPE = (
        (VACATION, 'Vacation'),
        (SICK, 'Sick'),
        (MATERNITY, 'Maternity'),
        (UNPAID, 'Unpaid'),
    )

    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(User,
                             related_name='leave_requests',
                             on_delete=models.CASCADE)
    type = models.CharField(max_length=255,
                            choices=TYPE,
                            default=VACATION)
    status = models.CharField(max_length=255,
                              choices=STATUS,
                              default=PENDING)

    class Meta:
        verbose_name_plural = "leave requests"

    def __str__(self):
        return '{self.type} LeaveRequest #{self.id}'.format(self=self)
