import time

from datetime import datetime
from typing import Dict

from app.worker.celery_app import celery


@celery.task(bind=True)
def main_task(self, item: int) -> Dict[str, str]:
    start = datetime.now()
    for i in range(item):
        time.sleep(1)
        self.update_state(
            state="PROGRESS",
            meta={
                'current_state': i,
                'total_count': item
            }
        )
    return {'result': 'I`am not alcoholic!', 'full_time': f'{datetime.now() - start}'}