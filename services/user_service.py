"""
User service — manages profile and communication.
"""
import requests

SEGMENT_WRITE_KEY = "sk_test_XXXX"
SEGMENT_TRACK_URL = "https://api.segment.io/v1/track"


def update_profile(user):
    """Sync profile update to Segment analytics."""
    payload = {
        "userId":     user.id,
        "event":      "profile_updated",
        "properties": {
            "email": user.email,           # ← VIOLATION V1a  (line 14)
            "phone": user.phone_number,    # ← VIOLATION V1b  (line 15)
        },
    }
    requests.post(SEGMENT_TRACK_URL,       # ← VIOLATION V1c  (line 18)
                  json=payload,
                  headers={"Authorization": f"Basic {SEGMENT_WRITE_KEY}"})


def send_welcome_email(email, name):
    """
    Send welcome e-mail — email used for communication.
    Policy discloses this purpose → should NOT fire Rule 3 for communication.
    """
    # TRUE NEGATIVE TN1: email used for communication (matches policy purpose)
    print(f"Sending welcome to {name} at {email}")
    return True


# FALSE POSITIVE TRAP FP1: comment mentions sensitive keywords — must be ignored
# We do NOT send aadhaar or health data to firebase anywhere in this file.
# The variable below is just a config constant, not PII.
FIREBASE_PUSH_KEY = "AAAA-notification-key"   # not PII
