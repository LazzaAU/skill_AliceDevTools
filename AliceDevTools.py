from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class AliceDevTools(AliceSkill):
	"""
	Author: LazzaAU
	Description: Tools used to assist dev&#39;n that suspect wouldnt make pa pull request
	"""


	@IntentHandler('MyIntentName')
	def testIntent(self, session: DialogSession, **_kwargs):
		pass


	@IntentHandler('MySecondIntentName')
	def secondTestIntent(self, session: DialogSession, **_kwargs):
		pass