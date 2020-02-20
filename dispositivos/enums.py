# sistema operacional dos dispositivos


class DispositivosEnum(object):
    ANDROID = 'ANDROID'
    IOS = 'IOS'

    @classmethod
    def choices(cls):
        return (
            (cls.ANDROID, 'Android'),
            (cls.IOS, 'iOS')
        )

# dispositivos disponiveis para emprestino ios
# dispositivos disponiveis para emprestino android
