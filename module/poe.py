import requests
import random
import json
import time
import re
ids = lambda  : "".join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890').lower() for x in range(64)])
apiUrl = 'https://www.quora.com/poe_api/gql_POST'
def sendMessage(message,cookies={'m-login': '1', 'm-b': 'K3K-BONrFG2mrC_PHjv74A==', 'm-b_lax': 'K3K-BONrFG2mrC_PHjv74A==', 'm-b_strict': 'K3K-BONrFG2mrC_PHjv74A==', 'm-s': 'Zj1lx6OJRMIjiw-I09f6-w==', 'm-uid': '2282320717', 'm-lat': 'ijdVLEyGRY0S4EWMADF3naqStyr9PAWC3ndXB0uqTQ=='}):
    ses = requests.Session()
    ses.cookies.update(cookies)
    response1 = ses.get('https://www.quora.com/poe_api/settings',headers={'accept-encoding': 'gzip','user-agent': 'okhttp/4.12.0'})
    formkey = response1.json()['formkey']
    tchannelData = response1.json()['tchannelData']
    minsek = tchannelData['minSeq']
    headers={
                "Host": "www.quora.com",
                "X-Apollo-Operation-ID": ids(),
                "X-Apollo-Operation-Name": "SendVerificationCodeForLoginMutation",
                "Accept": "multipart/mixed; deferSpec=20220824, application/json",
                "Quora-Formkey": formkey,
                "Quora-Tchannel": "poe-chan69-8888-rrdehrrpylexqekcvtyd",
                "User-Agent": "Poe a2.40.8 rv:4018 env:prod (SM-N960N; Android OS 9; in_ID)",
                "Poe-Language-Code": "in",
                "Content-Type": "application/json",
                "Content-Length": "358",
                "Accept-Encoding": "gzip"
            }
    # channelHash = tchannelData['channelHash']
    # response1=ses.post(apiUrl,
    #          headers=headers,
    #          json={
    #             "operationName": "SendVerificationCodeForLoginMutation",
    #             "variables": {
    #                 "emailAddress":email,
    #                 "phoneNumber": None
    #             },
    #             "query": "mutation SendVerificationCodeForLoginMutation($emailAddress: String, $phoneNumber: String) { sendVerificationCode(verificationReason: login, emailAddress: $emailAddress, phoneNumber: $phoneNumber) { status errorMessage } }"
    #             })
    # code = input('code : ')
    # headers.update({"X-Apollo-Operation-ID": ids()})
    # response2 = ses.post(apiUrl,
    #          headers=headers,
    #          json={
    #             "operationName": "LoginWithVerificationCodeMutation",
    #             "variables": {
    #                 "verificationCode": code,
    #                 "emailAddress": email,
    #                 "phoneNumber": None
    #             },
    #             "query": "mutation LoginWithVerificationCodeMutation($verificationCode: String!, $emailAddress: String, $phoneNumber: String) { loginWithVerificationCode(verificationCode: $verificationCode, emailAddress: $emailAddress, phoneNumber: $phoneNumber) { status errorMessage } }"
    #             })
    # headers.update({"X-Apollo-Operation-ID": ids()})
   
    headers.update({"X-Apollo-Operation-ID": ids()})
    #print(response3.json())
    
    response4 = ses.post(apiUrl,
                         headers=headers,
                         json={
                            "operationName": "MessageEdgeCreateMutation",
                            "variables": {
                                "chatId": None,
                                "attachments": None,
                                "bot": "web_search",
                                "query": message,
                                "source": {
                                "sourceType": "chat_input",
                                "chatInputMetadata": {
                                    "useVoiceRecord": False,
                                    "newChatContext": None
                                }
                                },
                                "messagePointPrice": 40,
                                "existingMessageAttachmentsIds": None
                            },
                            "query": "mutation MessageEdgeCreateMutation($chatId: BigInt, $attachments: [String!], $bot: String!, $query: String!, $source: MessageSource, $messagePointPrice: Int, $existingMessageAttachmentsIds: [BigInt!]) { messageEdgeCreate(attachments: $attachments, chatId: $chatId, bot: $bot, query: $query, source: $source, messagePointsDisplayPrice: $messagePointPrice, existingMessageAttachmentsIds: $existingMessageAttachmentsIds) { status statusMessage chat { __typename id chatId ...ChatFragment defaultBotObject { id shouldHide } } message { id node { __typename id ...MessageFragment } } chatBreak { id node { __typename id ...MessageFragment } } viewer { id messagePointInfo { __typename id ...MessagePointInfoFragment } } } }  fragment BotImageInfoFragment on Bot { id botImageInfo { assetTypeToUse localAssetName remoteAssetUrl } }  fragment BotCreatorFragment on PoeUser { id __typename uid handle profilePhotoUrl }  fragment BotMessagePointLimitFragment on MessagePointLimit { id balanceTooltipText displayMessagePointPrice fixedMessageLimit numRemainingMessages remainingMessagesLimitReason shouldShowReminderBanner }  fragment BotFragment on Bot { __typename botId ...BotImageInfoFragment baseModelDisplayName canUserAccessBot conversationStarters(count: 2) creator { __typename id ...BotCreatorFragment } deletionState description disclaimerText displayName followerCount hasSuggestedReplies id introduction isCreatedByPoeUserAccount isDown isOfficialBot isPromptPublic isServerBot isTrustedBot limitedAccessType messagePointLimit { __typename id ...BotMessagePointLimitFragment } messageTimeoutSecs nickname handle poweredBy promptPlaintext serverBotDependenciesLimitsString shareLink shouldHideLimitedAccessTag supportsFileUpload uploadFileSizeLimit viewerIsCreator viewerIsFollower translatedBotTags allowsImageAttachments monthlyActiveUsers supportsResend supportsRemix }  fragment ChatFragment on Chat { id chatId defaultBotObject { __typename ...BotFragment } lastInteractionTime membersIncludeUntrustedBot membersConnection { edges { node { __typename id ... on Bot { __typename botId deletionState displayName messagePointLimit { __typename ...BotMessagePointLimitFragment } ...BotImageInfoFragment } } } } title isDeleted }  fragment MessageAttachmentFragment on MessageAttachment { id name url file { size mimeType height width thumbnailUrl } isInline attachmentId }  fragment MessageAttachmentsFragment on Message { attachments { __typename id ...MessageAttachmentFragment } }  fragment MessageBotHeaderFragment on Message { bot { __typename id botId ...BotImageInfoFragment displayName deletionState handle supportsResend supportsRemix } }  fragment MessageRecommendedBotsFragment on Bot { __typename id ...BotImageInfoFragment displayName }  fragment MessageFragment on Message { __typename id messageId text authorNickname sourceType state suggestedReplies vote hasCitations ...MessageAttachmentsFragment creationTime ...MessageBotHeaderFragment recommendedBots { __typename id ...MessageRecommendedBotsFragment } }  fragment MessagePointInfoFragment on MessagePointInfo { id dailyMessagePointsAvailable messagePointBalance messagePointResetTime messagePointUsage maxDailyTopUpAmount subscriberBonusGrantResetTime totalMessagePointAllotment }"
                            })
    print(response4.json()) #['data']["messageEdgeCreate"]['chat']["chatId"])
    headers.update({"X-Apollo-Operation-ID": ids()})
    while True:
        response5 = ses.post(apiUrl,
                            headers=headers,
                            json={
                                "operationName": "ChatListQuery",
                                "variables": {
                                    "first": 5,
                                    "after": None,
                                    "botId": None
                                },
                                "query": "query ChatListQuery($first: Int, $after: String, $botId: BigInt) { chats(first: $first, after: $after, botId: $botId) { pageInfo { hasNextPage } edges { id node { __typename id chatId ...ChatListChatFragment messagesConnection(last: 2) { id edges { id node { __typename id ...ChatListMessageFragment } } } } } } }  fragment BotImageInfoFragment on Bot { id botImageInfo { assetTypeToUse localAssetName remoteAssetUrl } }  fragment BotMessagePointLimitFragment on MessagePointLimit { id balanceTooltipText displayMessagePointPrice fixedMessageLimit numRemainingMessages remainingMessagesLimitReason shouldShowReminderBanner }  fragment ChatListBotFragment on Bot { __typename id botId ...BotImageInfoFragment deletionState displayName messagePointLimit { __typename id ...BotMessagePointLimitFragment } }  fragment ChatListChatFragment on Chat { id chatId defaultBotObject { __typename id ...ChatListBotFragment } lastInteractionTime title isDeleted }  fragment ChatListMessageFragment on Message { id text authorNickname creationTime }"
                                })
        result = response5.json()['data']['chats']['edges'][0]
        try:
            balas = result['node']["messagesConnection"]['edges'][1]['node']['text']
            if balas:
                print(balas)
                print(ses.cookies.get_dict())
                break
        except Exception as e:print(e)
def login(email):
    ses = requests.Session()
    response1 = ses.get('https://www.quora.com/poe_api/settings',headers={'accept-encoding': 'gzip','user-agent': 'okhttp/4.12.0'})
    formkey = response1.json()['formkey']
    tchannelData = response1.json()['tchannelData']
    minsek = tchannelData['minSeq']
    headers={
                "Host": "www.quora.com",
                "X-Apollo-Operation-ID": ids(),
                "X-Apollo-Operation-Name": "SendVerificationCodeForLoginMutation",
                "Accept": "multipart/mixed; deferSpec=20220824, application/json",
                "Quora-Formkey": formkey,
                "Quora-Tchannel": "poe-chan69-8888-rrdehrrpylexqekcvtyd",
                "User-Agent": "Poe a2.40.8 rv:4018 env:prod (SM-N960N; Android OS 9; in_ID)",
                "Poe-Language-Code": "in",
                "Content-Type": "application/json",
                "Content-Length": "358",
                "Accept-Encoding": "gzip"
            }
    response1=ses.post(apiUrl,
             headers=headers,
             json={
                "operationName": "SendVerificationCodeForLoginMutation",
                "variables": {
                    "emailAddress":email,
                    "phoneNumber": None
                },
                "query": "mutation SendVerificationCodeForLoginMutation($emailAddress: String, $phoneNumber: String) { sendVerificationCode(verificationReason: login, emailAddress: $emailAddress, phoneNumber: $phoneNumber) { status errorMessage } }"
                })
    time.sleep(1)
    print(response1.json())
    code = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={email.split("@")[0]}&domain={email.split("@")[1]}').json()[0]['id']
    code = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={email.split("@")[0]}&domain={email.split("@")[1]}&id={code}').json()['body']
    code = re.findall("text-align:center;color:#333333;\">(.*?)</div></td></tr><tr>",code)[1]
    print(code)
    print(headers)
    headers.update({"X-Apollo-Operation-ID": ids()})
    response2 = ses.post(apiUrl,
             headers=headers,
             json={
                "operationName": "SignupWithVerificationCodeMutation",
                "variables": {
                    "verificationCode": code,
                    "emailAddress": email,
                    "phoneNumber": None,
                    "birthday": None,
                    "agreementResult": None
                },
                "query": "mutation SignupWithVerificationCodeMutation($verificationCode: String, $emailAddress: String, $phoneNumber: String, $birthday: String, $agreementResult: AgreementResults) { signupWithVerificationCode(verificationCode: $verificationCode, emailAddress: $emailAddress, phoneNumber: $phoneNumber, birthday: $birthday, agreementResults: $agreementResult) { status errorMessage } }"
                })
    response3 = ses.post(apiUrl,
                         headers=headers,
                         json={
                            "operationName": "ViewerInfoQuery",
                            "variables": {},
                            "query": "query ViewerInfoQuery { viewer { __typename id uid encryptedUidForAndroid appleOauthState hasCompletedMultiplayerNux ...ViewerStateUpdateFragment } }  fragment ViewerInfoPoeUserFragment on PoeUser { id __typename uid bio handle fullName followerCount followeeCount profilePhotoUrl viewerIsFollowing viewerIsFollowedBy }  fragment PoeSubscriptionFragment on Subscription { id expiresTime isActive isComplimentary isFreeTrial planType purchaseType willCancelAtPeriodEnd }  fragment BotImageInfoFragment on Bot { id botImageInfo { assetTypeToUse localAssetName remoteAssetUrl } }  fragment BotCreatorFragment on PoeUser { id __typename uid handle profilePhotoUrl }  fragment BotMessagePointLimitFragment on MessagePointLimit { id balanceTooltipText displayMessagePointPrice fixedMessageLimit numRemainingMessages remainingMessagesLimitReason shouldShowReminderBanner }  fragment BotFragment on Bot { __typename botId ...BotImageInfoFragment baseModelDisplayName canUserAccessBot conversationStarters(count: 2) creator { __typename id ...BotCreatorFragment } deletionState description disclaimerText displayName followerCount hasSuggestedReplies id introduction isCreatedByPoeUserAccount isDown isOfficialBot isPromptPublic isServerBot isTrustedBot limitedAccessType messagePointLimit { __typename id ...BotMessagePointLimitFragment } messageTimeoutSecs nickname handle poweredBy promptPlaintext serverBotDependenciesLimitsString shareLink shouldHideLimitedAccessTag supportsFileUpload uploadFileSizeLimit viewerIsCreator viewerIsFollower translatedBotTags allowsImageAttachments monthlyActiveUsers supportsResend supportsRemix }  fragment DefaultBotFragment on Bot { __typename id botId displayName ...BotImageInfoFragment }  fragment MessagePointInfoFragment on MessagePointInfo { id dailyMessagePointsAvailable messagePointBalance messagePointResetTime messagePointUsage maxDailyTopUpAmount subscriberBonusGrantResetTime totalMessagePointAllotment }  fragment ViewerStateUpdateFragment on Viewer { id __typename primaryEmail autoGeneratedHandle poeUser { __typename id ...ViewerInfoPoeUserFragment } hasCompletedMultiplayerNux subscription { __typename id ...PoeSubscriptionFragment } advertisedSubscriptionBots { __typename id displayName providerName ...BotImageInfoFragment } subscriptionMessageLimitExplanationText appRatingPromptInfo { prePromptInfo { state totalImpressions lastImpressionTime } } androidMinSupportedVersion: integerGate(gateName: \"poe_android_min_supported_version\") androidMinEncouragedVersion: integerGate(gateName: \"poe_android_min_encouraged_version\") availableBotsConnection(first: 1, includeNewModel: true) { id edges { id node { __typename id ...BotFragment } } } defaultBot { __typename id ...DefaultBotFragment } messagePointInfo { __typename id ...MessagePointInfoFragment } enableMultiBotV0MinVersion: integerGate(gateName: \"poe_android_enable_multibot_v0_min_build_number\") enableVideoAttachmentPlayerV2: integerGate(gateName: \"poe_android_video_attachment_v2_min_build_number\") enableMessageResendMinVersion: integerGate(gateName: \"poe_android_resend_min_build_number\") enableBlockingEmailInputModalMinVersion: integerGate(gateName: \"poe_android_show_blocking_email_input_modal_min_build_number\") enableVideoUpload: integerGate(gateName: \"poe_android_video_upload_min_build_number\") enableExploreBotsRedesign: integerGate(gateName: \"poe_android_explore_bots_redesign_min_build_number\") enableBotInfoCardRedesign: integerGate(gateName: \"poe_android_bot_info_card_redesign_min_build_number\") enableMessageRemix: integerGate(gateName: \"poe_android_remix_min_build_number\") enableMultiBotV1MinVersion: integerGate(gateName: \"poe_android_enable_multibot_v1_min_build_number\") enableConversationStarters: integerGate(gateName: \"poe_android_conversation_starters_min_build_number\") allowAttachmentOnlyMessages: integerGate(gateName: \"poe_android_allow_sending_attachment_only_messages\") enablePayPerMessageMinVersion: integerGate(gateName: \"poe_android_pay_per_message_min_build_number\") enableMessageUpdateThrottling: integerGate(gateName: \"poe_android_throttle_message_update_min_build_number\") messageUpdateIntervalMilliseconds: integerGate(gateName: \"poe_android_throttle_message_update_threshold_milliseconds\") enableInChatRecommendations: integerGate(gateName: \"poe_android_in_chat_recommendations_min_build_number\") enableShareBotOrChatModalMinVersion: integerGate(gateName: \"poe_android_share_bot_or_chat_modal_min_build_number\") enableChatPerf: integerGate(gateName: \"poe_android_chat_perf_min_build_number\") enableLowPriorityMarkdownParsing: integerGate(gateName: \"poe_android_low_priority_markdown_parsing_min_build_number\") enableRedesignedLoginScreen: integerGate(gateName: \"poe_android_login_redesign_min_build_number\") externalUrlSubstrings isEligibleForAndroidSubscriptions isEligibleToPurchaseOnAnyPlatform showConversationStarters announcement availableSubscriptionOfferFeatures { id monthlyPointsGrant includedItemStrings } }"
                            })
    return ses.cookies.get_dict()
    
sendMessage('hasil pemilihan presiden indonesia 2024',cookies={'m-login': '1', 'm-b': '4Hf09ae_0VY86_21fqPOqg==', 'm-b_lax': '4Hf09ae_0VY86_21fqPOqg==', 'm-b_strict': '4Hf09ae_0VY86_21fqPOqg==', 'm-s': '5Pl_SBlmfcx5xXuLDwXLWQ==', 'm-uid': '2574331198', 'm-lat': 'Npqa1McCv/qNLTwo9Lsxm9MLjdjebCIjmqixak+grA=='})
#print(login('kfdfddseekj7fgg4u7c3@vjuum.com'))