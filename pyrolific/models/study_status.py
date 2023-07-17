from enum import Enum


class StudyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    AWAITING_REVIEW = "AWAITING REVIEW"
    COMPLETED = "COMPLETED"
    PAUSED = "PAUSED"
    SCHEDULED = "SCHEDULED"
    UNPUBLISHED = "UNPUBLISHED"
    PUBLISHING = "PUBLISHING"  # not in docs

    def __str__(self) -> str:
        return str(self.value)
