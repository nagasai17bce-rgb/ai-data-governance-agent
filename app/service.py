import re

class Service:
    def run(self, value: str):
        fields = [x.strip() for x in value.split(",") if x.strip()]
        findings = [
            {"field": f, "classification": "sensitive", "action": "restrict_or_mask"}
            for f in fields if re.search(r"(email|phone|ssn|address)", f, re.I)
        ]
        return {"fields": fields, "findings": findings, "approval_required": bool(findings)}
