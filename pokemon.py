import random


class Pokemon():
	def __init__(self, data: dict):
		self.data = {}
		self.data.update(data)
		
	def set_ivs(self, num_perfect=0):
		'''
		According to https://www.reddit.com/r/pokemontrades/comments/6a3xip/dont_bother_trying_to_catch_a_56iv_pokemon_via/:
		(by /u/blackaurora)
		
		[info]
		It's been confirmed that getting a 5-6IV Pokemon via SOS chaining is nearly impossible, as some have suspected.
		
		It turns out that the way the game is coded, getting a 5IV Pokemon in a SOS chain is no more likely than getting a 5IV Pokemon without chaining. So, possible, sure - but you're looking at 1/33554432 ~1/5772805 odds for 5IV and 1/1073741824 for 6IV.
		
		For those interested in the why: it generates the IVs first, then bumps up the amount of 31s if it's less than 4IV (or 1IV/2IV/3IV depending on where you are in the chain). See lines 59-63 of this pastebin* of the game's code (thanks Kaphotics).
		
		Translation: If you chain past 30 Pokemon, and find a wild Pokemon whose original IVs are say 1/2/31/4/5/6, it will only add three more random 31s. So, it could be 31/31/31/31/5/6, but will never be 31/31/31/31/31/6, 31/2/31/31/31/31, or any other 5IV spread.
		
		In other words, if you want a legitimate 5-6IV Ditto, stick with RNGing.
		
		*The relevant code: (lines 59-63):
		
		59	while ( pml::pokepara::CoreParam::GetTalentPowerMaxNum(v4) < v12 )
   		60	{
		61		v13 = gfl2::math::SFMTRandom::Next((v3 + 16), 6u);
		62		pml::pokepara::CoreParam::ChangeTalentPower(v4, v13, 31);
		63	}
		
		which appears to be equivalent to
		
		while num_perfect_ivs < num_guaranteed_ivs:
			n = random.randrange(6)
			ivs[n] = 31
		
		I'm choosing to implement this a bit differently. Instead, we'll choose the four (or however many) perfect IVs, then
		randomly generate the others.
		'''
		
		keys = ('iv_hp', 'iv_atk', 'iv_def', 'iv_spa', 'iv_spd', 'iv_spe')
		perfect = random.sample(keys, num_perfect)
		
		for key in keys:
			self.data.update(key, 31 if key in perfect else random.randrange(32))
		
