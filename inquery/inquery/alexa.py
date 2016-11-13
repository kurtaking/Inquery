from __future__ import absolute_import
from django_alexa.api import intent, ResponseBuilder


@intent
def LaunchRequest(**kwargs):
    """
    Default Start Session Intent
    ---
    launch
    open
    resume
    start
    run
    load
    begin
    """
    print("Make it here")

    return ResponseBuilder.create_response(message="Welcome.",
                                           reprompt="What would you like to do next?",
                                           end_session=False)


@intent
def CancelIntent(**kwargs):
    """
    Default Cancel Intent
    ---
    cancel
    """
    print("Make it here")
    return ResponseBuilder.create_response(message="Canceling actions not configured!",
                                           reprompt="What would you like to do next?",
                                           end_session=False)


@intent
def StopIntent(**kwargs):
    """
    Default Stop Intent
    ---
    stop
    end
    nevermind
    """
    print("Make it here")
    return ResponseBuilder.create_response(message="Stopping actions not configured!")


@intent
def HelpIntent(**kwargs):
    """
    Default Help Intent
    ---
    help
    info
    information
    """
    print("Make it here")
    return ResponseBuilder.create_response(message="No help was configured!")


@intent
def SessionEndedRequest(**kwargs):
    """
    Default End Session Intent
    ---
    quit
    """
    print("Make it here")
    return ResponseBuilder.create_response()