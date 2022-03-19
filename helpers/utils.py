import uuid
import random

SIX_NUMBER = random.randint(100000, 999999)
UNIQUE_TRAKING_NUMBER = str(uuid.uuid4()).replace('-', '').upper()[:12]
