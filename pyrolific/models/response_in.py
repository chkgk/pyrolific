from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.question_response import QuestionResponse
    from ..models.section import Section


T = TypeVar("T", bound="ResponseIn")


@attr.s(auto_attribs=True)
class ResponseIn:
    """The model used to create a `Response`.

    Attributes:
        participant_id (str): The Prolific participant ID. Example: 62908f0b98a55b36ac68b992.
        submission_id (str): The Prolific submission ID. Example: 62908f0b98a55b36ac68b992.
        sections (Union[Unset, List['Section']]): An array of sections from the survey, otherwise use `questions`.
        questions (Union[Unset, List['QuestionResponse']]): An array of questions from the survey, otherwise use
            `sections`.
    """

    participant_id: str
    submission_id: str
    sections: Union[Unset, List["Section"]] = UNSET
    questions: Union[Unset, List["QuestionResponse"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        participant_id = self.participant_id
        submission_id = self.submission_id
        sections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()

                sections.append(sections_item)

        questions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.questions, Unset):
            questions = []
            for questions_item_data in self.questions:
                questions_item = questions_item_data.to_dict()

                questions.append(questions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "participant_id": participant_id,
                "submission_id": submission_id,
            }
        )
        if sections is not UNSET:
            field_dict["sections"] = sections
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.question_response import QuestionResponse
        from ..models.section import Section

        d = src_dict.copy()
        participant_id = d.pop("participant_id")

        submission_id = d.pop("submission_id")

        sections = []
        _sections = d.pop("sections", UNSET)
        for sections_item_data in _sections or []:
            sections_item = Section.from_dict(sections_item_data)

            sections.append(sections_item)

        questions = []
        _questions = d.pop("questions", UNSET)
        for questions_item_data in _questions or []:
            questions_item = QuestionResponse.from_dict(questions_item_data)

            questions.append(questions_item)

        response_in = cls(
            participant_id=participant_id,
            submission_id=submission_id,
            sections=sections,
            questions=questions,
        )

        response_in.additional_properties = d
        return response_in

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
