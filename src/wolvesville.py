from requests import Session

class WolvesVille:
	def __init__(
			self,
			platform: str = "android",
			locale: str = "ru") -> None:
		self.api = "https://api-game.wolvesville.com/api"
		self.core_api = "https://core.api-wolvesville.com"
		self.auth_api = "https://api-auth.wolvesville.com"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "okhttp/3.12.12"
		}
		self.locale = locale
		self.platform = platform
		self.version_number = 4194708

	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self.session.get(endpoint, params=params).json()

	def _post(self, endpoint: str, data: dict = None) -> dict:
		return self.session.post(endpoint, json=data).json()

	def login(self, email: str, password: str) -> dict:
		data = {
			"email": email,
			"password": password
		}
		response = self._post(
			f"{self.auth_api}/players/signInWithEmailAndPassword", data)
		if "idToken" in response:
			self.id_token = response["idToken"]
			self.session.headers["Authorization"] = f"Bearer {self.token}"
		return response

	def sign_up_with_email_and_password(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password,
			"locale": self.locale
		}
		return self._post(
			f"{self.auth_api}/players/signUpWithEmailAndPassword", data)

	def register(
			self,
			username: str,
			token: str,
			gender: str = "MALE") -> dict:
		data = {
			"username": username,
			"token": token,
			"gender": gender,
			"locale": self.locale,
			"versionNumber": self.version_number,
			"platform": self.platform
		}
		return self._post(
			f"{self.core_api}/register", data)

	def claim_daily_reward(self) -> dict:
		return self._post(f"{self.core_api}/dailyRewards")

	def change_password(self, password: str) -> dict:
		data = {
			"password": password,
			"idToken": self.id_token
		}
		return self._post(
			f"{self.core_api}/players/changePassword", data)

	def redeem_voucher(self, code: str) -> dict:
		data = {
			"code": code
		}
		return self._post(
			f"{self.core_api}/vouchers/redeem", data)

	def get_friend_invitation_rewards(self) -> dict:
		return self._get(
			f"{self.core_api}/players/friendInvitationRewards")

	def get_purchases(self) -> dict:
		return self._get(
			f"{self.core_api}/billing/purchases")

	def get_support_pins(self) -> dict:
		return self._get(f"{self.core_api}/supportPins")

	def refresh_support_pins(self) -> dict:
		return self._post(
			f"{self.core_api}/supportPins/refresh")

	def get_sent_gifts(self) -> dict:
		return self._get(
			f"{self.core_api}/billing/gifts/sent")

	def get_received_gifts(self) -> dict:
		return self._get(
			f"{self.core_api}/billing/gifts/received")

	def get_rotating_limited_offers(self) -> dict:
		return self._get(
			f"{self.core_api}/billing/rotatingLimitedOffers")

	def get_pending_friend_requests(self) -> dict:
		return self._get(
			f"{self.core_api}/friendRequests/pending")

	def get_friends_list(self) -> dict:
		return self._get(f"{self.core_api}/friends")

	def get_season_and_battlepasses(self) -> dict:
		return self._get(
			f"{self.core_api}/battlePass/seasonAndBattlePass")

	def get_daily_rewards_list(self) -> dict:
		return self._get(f"{self.core_api}/dailyRewards")

	def get_wheel_items(self) -> dict:
		return self._get(
			f"{self.core_api}/rewards/wheelItems/v2")

	def get_calendars(self) -> dict:
		return self._get(f"{self.core_api}/calendars")

	def get_inventory(self) -> dict:
		return self._get(f"{self.core_api}/inventory")

	def get_equipped_items(self) -> dict:
		return self._get(f"{self.core_api}/equippedItems")

	def get_role_cards_abilities(self) -> dict:
		return self._get(
			f"{self.core_api}/roleCards/abilities")

	def get_total_win_count(self) -> dict:
		return self._get(
			f"{self.core_api}/playerRoleStats/totalWinCount")

	def get_annoucements(self, limit: int = 1) -> dict:
		return self._get(
			f"{self.core_api}/announcements/v2?limit={limit}")

	def get_blocked_players(self) -> dict:
		return self._get(f"{self.core_api}/blockedPlayers")

	def get_claimable_rewards(self) -> dict:
		return self._get(
			f"{self.core_api}/challenges/claimAbleRewards")

	def get_clans_open_requests(self) -> dict:
		return self._get(f"{self.core_api}/clans/openRequests")

	def get_inventory_hidden_item_ids(self) -> dict:
		return self._get(f"{self.core_api}/inventory/hiddenItemIds")

	def get_owned_role_cards(self) -> dict:
		return self._get(f"{self.core_api}/roleCards/owned")

	def get_gamemode_info(self, gamemode: str) -> dict:
		return self._get(
			f"{self.core_api}/roleRotation/funGameMode/{gamemode}")

	def get_inventory_slot_price(self) -> dict:
		return self._get(f"{self.core_api}/inventory/slotPrice")

	def check_app_cache(self) -> dict:
		return self._get(f"{self.core_api}/appCache/check")

	def get_active_game_modes(self) -> dict:
		return self._get(f"{self.api}/public/activeGameModes/v2")
