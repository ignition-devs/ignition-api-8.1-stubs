from typing import List

from dev.coatl.helper.types import AnyStr

def loadFromFile(filePath: AnyStr, projectName: AnyStr, mode: int) -> None: ...
def removeGroups(projectName: AnyStr, paths: List[AnyStr]) -> None: ...
