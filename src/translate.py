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
translatedText = argostranslate.translate.translate("just testing to see how well this.", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("just testing to see how well this program really works.", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("just testing to see how well this program really works. i wonder how well this program.", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("just testing to see how well this program really works. i wonder how well this program does work.", from_code, to_code)
print(translatedText)

text = "just testing to see how well this program really works. i wonder how well this program does work."
print(text.count("."))

translatedText = argostranslate.translate.translate("just testing to see how well this program really works i wonder how well this program does work", from_code, to_code)
print(translatedText)

translatedText = argostranslate.translate.translate("this is mister smith.", from_code, to_code)
print(translatedText)