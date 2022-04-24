from django.db.models import F


def get_max_seq(model):
    query = model.objects.all()
    max_seq = max([i.seq for i in query])
    return max_seq


def set_seq(model):
    max_seq = get_max_seq(model)
    return max_seq+1


def seq_plus(model):
    plus = model.objects.all().update(seq=F("seq") + 1)
    return plus
