import os
from pathlib import Path
import pandas as pd
import logging
from typing import Optional, Union
from error_messages import DataReadingErrorMessages as EM, SUPPORTED_FILE_EXTENSIONS

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DataLoader:
    def load_data(self, file_path: Union[str, Path]) -> Optional[pd.DataFrame]:
        """
        Load data from a CSV file.
        """

        if not isinstance(file_path, (str, Path)):
            logger.error(EM.INVALID_FILE_PATH_TYPE.value.format(type=type(file_path)))
            raise TypeError(
                EM.INVALID_FILE_PATH_TYPE.value.format(type=type(file_path))
            )
        if not Path(file_path).exists():
            logger.error(EM.FILE_NOT_FOUND.value.format(file_path=file_path))
            raise FileNotFoundError(EM.FILE_NOT_FOUND.value.format(file_path=file_path))

        ext = Path(file_path).suffix

        if ext not in SUPPORTED_FILE_EXTENSIONS:
            logger.error(
                EM.EXT_NOT_SUPPORTED.value.format(
                    ext=ext, supported_extensions=SUPPORTED_FILE_EXTENSIONS
                )
            )
            raise ValueError(
                EM.EXT_NOT_SUPPORTED.value.format(
                    ext=ext, supported_extensions=SUPPORTED_FILE_EXTENSIONS
                )
            )

        data = pd.read_csv(file_path)
        if data.empty:
            logger.error(EM.EMPTY_DATA_FILE.value)
            raise ValueError(EM.EMPTY_DATA_FILE.value)
