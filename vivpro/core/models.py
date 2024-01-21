from django.db import models

# Create your models here.


class MusicTrack(models.Model):
    """
    Model representing a music track with various attributes.
    Attributes:
        index (postive integer field which we accepts for the data. should be unique)
        id (CharField with primary key attribute): A unique identifier for the music track.
        title (CharField): The title of the music track.
        danceability (FloatField): A measure of the track's suitability for dancing.
        energy (FloatField): A measure of the intensity and activity of the track.
        key (IntegerField): The key the track is in.
        loudness (FloatField): The overall loudness of the track.
        mode (IntegerField): Modality of the track (major or minor).
        acousticness (FloatField): A measure of the acoustic characteristics of the track.
        instrumentalness (FloatField): A measure of whether the track is instrumental.
        liveness (FloatField): A measure of the presence of an audience in the recording.
        valence (FloatField): A measure of the musical positiveness of the track.
        tempo (FloatField): The overall estimated tempo of the track.
        duration_ms (IntegerField): The duration of the track in milliseconds.
        time_signature (IntegerField): The time signature of the track.
        num_bars (IntegerField): The number of musical bars in the track.
        num_sections (IntegerField): The number of sections in the track.
        num_segments (IntegerField): The number of segments in the track.
        class_field (CharField): A categorical class label for the track.
    """

    index = models.PositiveIntegerField(unique=True)
    id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    time_signature = models.IntegerField()
    num_bars = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    class_field = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "MusicTrack"
        indexes = [models.Index(fields=["title"])]

    def validate(self, *args, **kwargs):
        """Holds all validations needed before saving the music track instance"""
        if not self.rating:
            return

        if self.rating > 5:
            raise Exception("Max rating for a song is 5!")

    def save(self, *args, **kwargs) -> None:
        """Overrides core django model's save method to add before and after save methods"""
        self.validate(*args, **kwargs)
        super().save(*args, **kwargs)
