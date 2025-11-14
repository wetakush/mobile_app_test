from pythonforandroid.recipe import Recipe


class LibffiRecipe(Recipe):
    name = 'libffi'

    def should_build(self, arch):
        return False  # отключаем сборку полностью
