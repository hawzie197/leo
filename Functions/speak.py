from subprocess import call

def say(answer):
    """
    Speaks the ending result to the user
    """
    call(["espeak", "-v", "mb-us1", answer])
