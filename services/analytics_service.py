"""
Analytics service — product usage tracking.
"""
import mixpanel

BIOMETRIC_STORE = {}

mp = mixpanel.Mixpanel("TRACK_TOKEN_XXXX")


def track_location(user_id, location):
    """Track user location for heatmap analytics."""
    # VIOLATION V4: location PII sent to Mixpanel (not disclosed in policy)
    mp.track(user_id, "location_update", {   # line 14
        "location": location,                # line 15
    })


def save_biometric_hash(user_id, fingerprint_hash):
    """
    Store biometric hash for future face/finger auth.
    """
    # VIOLATION V5: biometric PII — completely absent from privacy policy (Rule 1 gap)
    BIOMETRIC_STORE[user_id] = fingerprint_hash   # line 23


def track_email_engagement(user_id, email):
    """Track email open events — email used for analytics (policy says communication only)."""
    # VIOLATION V6: email used for 'analytics' module type; policy states 'communication'
    # → Rule 3 Purpose–PII Linkage fires for email
    mp.track(user_id, "email_opened", {"email": email})   # line 30
