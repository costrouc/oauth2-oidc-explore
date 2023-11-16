# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\"\x82\x01\n\x06\x43lient\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06secret\x18\x02 \x01(\t\x12\x15\n\rredirect_uris\x18\x03 \x03(\t\x12\x15\n\rtrusted_peers\x18\x04 \x03(\t\x12\x0e\n\x06public\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x10\n\x08logo_url\x18\x07 \x01(\t\".\n\x0f\x43reateClientReq\x12\x1b\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x0b.api.Client\"G\n\x10\x43reateClientResp\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\x12\x1b\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x0b.api.Client\"\x1d\n\x0f\x44\x65leteClientReq\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x10\x44\x65leteClientResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"k\n\x0fUpdateClientReq\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rredirect_uris\x18\x02 \x03(\t\x12\x15\n\rtrusted_peers\x18\x03 \x03(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x10\n\x08logo_url\x18\x05 \x01(\t\"%\n\x10UpdateClientResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"J\n\x08Password\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\t\"4\n\x11\x43reatePasswordReq\x12\x1f\n\x08password\x18\x01 \x01(\x0b\x32\r.api.Password\",\n\x12\x43reatePasswordResp\x12\x16\n\x0e\x61lready_exists\x18\x01 \x01(\x08\"J\n\x11UpdatePasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08new_hash\x18\x02 \x01(\x0c\x12\x14\n\x0cnew_username\x18\x03 \x01(\t\"\'\n\x12UpdatePasswordResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"\"\n\x11\x44\x65letePasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"\'\n\x12\x44\x65letePasswordResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"\x11\n\x0fListPasswordReq\"4\n\x10ListPasswordResp\x12 \n\tpasswords\x18\x01 \x03(\x0b\x32\r.api.Password\"\x0c\n\nVersionReq\"*\n\x0bVersionResp\x12\x0e\n\x06server\x18\x01 \x01(\t\x12\x0b\n\x03\x61pi\x18\x02 \x01(\x05\"W\n\x0fRefreshTokenRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x03\x12\x11\n\tlast_used\x18\x06 \x01(\x03\"!\n\x0eListRefreshReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"?\n\x0fListRefreshResp\x12,\n\x0erefresh_tokens\x18\x01 \x03(\x0b\x32\x14.api.RefreshTokenRef\"6\n\x10RevokeRefreshReq\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"&\n\x11RevokeRefreshResp\x12\x11\n\tnot_found\x18\x01 \x01(\x08\"4\n\x11VerifyPasswordReq\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"9\n\x12VerifyPasswordResp\x12\x10\n\x08verified\x18\x01 \x01(\x08\x12\x11\n\tnot_found\x18\x02 \x01(\x08\x32\xc7\x05\n\x03\x44\x65x\x12=\n\x0c\x43reateClient\x12\x14.api.CreateClientReq\x1a\x15.api.CreateClientResp\"\x00\x12=\n\x0cUpdateClient\x12\x14.api.UpdateClientReq\x1a\x15.api.UpdateClientResp\"\x00\x12=\n\x0c\x44\x65leteClient\x12\x14.api.DeleteClientReq\x1a\x15.api.DeleteClientResp\"\x00\x12\x43\n\x0e\x43reatePassword\x12\x16.api.CreatePasswordReq\x1a\x17.api.CreatePasswordResp\"\x00\x12\x43\n\x0eUpdatePassword\x12\x16.api.UpdatePasswordReq\x1a\x17.api.UpdatePasswordResp\"\x00\x12\x43\n\x0e\x44\x65letePassword\x12\x16.api.DeletePasswordReq\x1a\x17.api.DeletePasswordResp\"\x00\x12>\n\rListPasswords\x12\x14.api.ListPasswordReq\x1a\x15.api.ListPasswordResp\"\x00\x12\x31\n\nGetVersion\x12\x0f.api.VersionReq\x1a\x10.api.VersionResp\"\x00\x12:\n\x0bListRefresh\x12\x13.api.ListRefreshReq\x1a\x14.api.ListRefreshResp\"\x00\x12@\n\rRevokeRefresh\x12\x15.api.RevokeRefreshReq\x1a\x16.api.RevokeRefreshResp\"\x00\x12\x43\n\x0eVerifyPassword\x12\x16.api.VerifyPasswordReq\x1a\x17.api.VerifyPasswordResp\"\x00\x42/\n\x12\x63om.coreos.dex.apiZ\x19github.com/dexidp/dex/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.coreos.dex.apiZ\031github.com/dexidp/dex/api'
  _globals['_CLIENT']._serialized_start=19
  _globals['_CLIENT']._serialized_end=149
  _globals['_CREATECLIENTREQ']._serialized_start=151
  _globals['_CREATECLIENTREQ']._serialized_end=197
  _globals['_CREATECLIENTRESP']._serialized_start=199
  _globals['_CREATECLIENTRESP']._serialized_end=270
  _globals['_DELETECLIENTREQ']._serialized_start=272
  _globals['_DELETECLIENTREQ']._serialized_end=301
  _globals['_DELETECLIENTRESP']._serialized_start=303
  _globals['_DELETECLIENTRESP']._serialized_end=340
  _globals['_UPDATECLIENTREQ']._serialized_start=342
  _globals['_UPDATECLIENTREQ']._serialized_end=449
  _globals['_UPDATECLIENTRESP']._serialized_start=451
  _globals['_UPDATECLIENTRESP']._serialized_end=488
  _globals['_PASSWORD']._serialized_start=490
  _globals['_PASSWORD']._serialized_end=564
  _globals['_CREATEPASSWORDREQ']._serialized_start=566
  _globals['_CREATEPASSWORDREQ']._serialized_end=618
  _globals['_CREATEPASSWORDRESP']._serialized_start=620
  _globals['_CREATEPASSWORDRESP']._serialized_end=664
  _globals['_UPDATEPASSWORDREQ']._serialized_start=666
  _globals['_UPDATEPASSWORDREQ']._serialized_end=740
  _globals['_UPDATEPASSWORDRESP']._serialized_start=742
  _globals['_UPDATEPASSWORDRESP']._serialized_end=781
  _globals['_DELETEPASSWORDREQ']._serialized_start=783
  _globals['_DELETEPASSWORDREQ']._serialized_end=817
  _globals['_DELETEPASSWORDRESP']._serialized_start=819
  _globals['_DELETEPASSWORDRESP']._serialized_end=858
  _globals['_LISTPASSWORDREQ']._serialized_start=860
  _globals['_LISTPASSWORDREQ']._serialized_end=877
  _globals['_LISTPASSWORDRESP']._serialized_start=879
  _globals['_LISTPASSWORDRESP']._serialized_end=931
  _globals['_VERSIONREQ']._serialized_start=933
  _globals['_VERSIONREQ']._serialized_end=945
  _globals['_VERSIONRESP']._serialized_start=947
  _globals['_VERSIONRESP']._serialized_end=989
  _globals['_REFRESHTOKENREF']._serialized_start=991
  _globals['_REFRESHTOKENREF']._serialized_end=1078
  _globals['_LISTREFRESHREQ']._serialized_start=1080
  _globals['_LISTREFRESHREQ']._serialized_end=1113
  _globals['_LISTREFRESHRESP']._serialized_start=1115
  _globals['_LISTREFRESHRESP']._serialized_end=1178
  _globals['_REVOKEREFRESHREQ']._serialized_start=1180
  _globals['_REVOKEREFRESHREQ']._serialized_end=1234
  _globals['_REVOKEREFRESHRESP']._serialized_start=1236
  _globals['_REVOKEREFRESHRESP']._serialized_end=1274
  _globals['_VERIFYPASSWORDREQ']._serialized_start=1276
  _globals['_VERIFYPASSWORDREQ']._serialized_end=1328
  _globals['_VERIFYPASSWORDRESP']._serialized_start=1330
  _globals['_VERIFYPASSWORDRESP']._serialized_end=1387
  _globals['_DEX']._serialized_start=1390
  _globals['_DEX']._serialized_end=2101
# @@protoc_insertion_point(module_scope)