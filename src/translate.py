import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "ja"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# Translate
translatedText = argostranslate.translate.translate("does this program work let us find out", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("does this program work? let us find out.", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("Does this program work? Let's find out.", from_code, to_code)
print(translatedText)