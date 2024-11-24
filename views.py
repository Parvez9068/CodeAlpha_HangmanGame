from django.shortcuts import render, redirect
import random

WORDS = ['python', 'django', 'programming', 'hangman', 'developer']

def index(request):
    if request.method == 'POST':
        if 'new_game' in request.POST:
            # Reset the session and start a new game
            request.session['word'] = random.choice(WORDS)
            request.session['guesses'] = ''
            request.session['attempts_left'] = 6
            return redirect('index')  # Redirect to the main page

        if 'exit' in request.POST:
            # Clear the session and redirect to an exit/landing page
            request.session.flush()
            return render(request, 'game/exit.html')  # Create an exit.html template

        # Handle guessing
        guess = request.POST.get('guess', '').lower()
        if 'word' not in request.session:
            request.session['word'] = random.choice(WORDS)
            request.session['guesses'] = ''
            request.session['attempts_left'] = 6

        word = request.session['word']
        guesses = request.session['guesses']
        attempts_left = request.session['attempts_left']

        if guess and guess not in guesses:
            guesses += guess
            request.session['guesses'] = guesses
            if guess not in word:
                attempts_left -= 1
                request.session['attempts_left'] = attempts_left

    # Prepare the game state
    word = request.session.get('word', random.choice(WORDS))
    guesses = request.session.get('guesses', '')
    attempts_left = request.session.get('attempts_left', 6)
    display_word = ''.join([char if char in guesses else '_' for char in word])

    context = {
        'display_word': display_word,
        'attempts_left': attempts_left,
        'guesses': guesses,
        'won': '_' not in display_word,
        'lost': attempts_left <= 0,
    }
    return render(request, 'game/index.html', context)
