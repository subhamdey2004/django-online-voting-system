from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Election, Candidate, Vote

@login_required
def vote_view(request):
    election = Election.objects.filter(is_active=True).first()
    if not election:
        return render(request, "vote.html", {"election": None})
    already_voted = Vote.objects.filter(
        voter=request.user,
        election=election
        ).exists()
    if request.method == "POST" and not already_voted:
        candidate_id = request.POST.get("candidate")
        if candidate_id:
            candidate = Candidate.objects.get(
                id=candidate_id,
                election=election
                )
            Vote.objects.create(
                voter=request.user,
                election=election,
                candidate=candidate
                )
            return redirect("results")
        candidates = Candidate.objects.filter(election=election)
        context = {
            "election": election,
            "candidates": candidates,
            "already_voted": already_voted
            }
        return render(request, "vote.html", context)
@login_required
def results_view(request):
    election = Election.objects.filter(is_active=True).first()
    candidates = []
    if election:
        candidates = Candidate.objects.filter(election=election)
        context = {
            "election": election,
            "candidates": candidates
            }
        return render(request, "results.html", context)

