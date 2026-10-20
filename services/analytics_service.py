import mixpanel

mixpanel_client = mixpanel.Mixpanel("TRACK_TOKEN_XXXX")

# In-memory storage used by this synthetic test repository.
BIOMETRIC_STORE = {}


def track_location(user_id, location):
    """Record a location-related product event."""
    mixpanel_client.track(user_id, "location_update", {
        "location": location,
    })


def save_biometric_hash(user_id, fingerprint_hash):
    data = {"biometric": fingerprint_hash}
    BIOMETRIC_STORE[user_id] = data


def track_email_open(user_id, email):
    """Record an email-related product event."""
    mixpanel_client.track(user_id, "email_opened", {
        "email": email,
    })
