from rout import ma

#Схема данных, для отображения и удобства в работе
class SportShema(ma.Schema):
    class Meta:
        fields = ('id', 'team', 'name', 'game', 'gold', 'silver', 'bronze')
