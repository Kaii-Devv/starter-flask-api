function(e) {
                        if ("string" != typeof e) throw new TypeError("expected string");
                        var a, n = unescape(encodeURIComponent(e)),
                            t = new Uint8Array(n.length);
                        for (a = 0; a < n.length; a++) t[a] = n.charCodeAt(a);
                        return t
                    }
function(e) {
                        var a, n = [];
                        for (a = 0; a < e.length; a++) n.push(String.fromCharCode(e[a]));
                        return decodeURIComponent(escape(n.join("")))
                    }
function(e) {
                        var a, n = [],
                            t = e.length;
                        for (a = 0; a < t; a++) n.push(String.fromCharCode(e[a]));
                        return btoa(n.join(""))
                    }
function(e) {
                        a(e);
                        var n, t = atob(e),
                            i = new Uint8Array(t.length);
                        for (n = 0; n < t.length; n++) i[n] = t.charCodeAt(n);
                        return i
                    }

function randomBytes(size, callback) {
  size = assertSize(size, 1, 0, Infinity);
  if (callback !== undefined) {
    validateFunction(callback, 'callback');
  }

  const buf = new FastBuffer(size);

  if (callback === undefined) {
    randomFillSync(buf.buffer, 0, size);
    return buf;
  }

  // Keep the callback as a regular function so this is propagated.
  randomFill(buf.buffer, 0, size, function(error) {
    if (error) return FunctionPrototypeCall(callback, this, error);
    FunctionPrototypeCall(callback, this, null, buf);
  });
}
function(e, a, n) {
                    var t = n.name,
                        i = void 0 === t ? "AES-GCM" : t,
                        o = n.iv,
                        c = n.additionalData,
                        f = void 0 === c ? new Uint8Array([]) : c,
                        v = n.tagLength;
                    return r(void 0, void 0, void 0, (function() {
                        var n;
                        return s(this, (function(t) {
                            if (m({
                                    name: i,
                                    iv: o,
                                    tagLength: v
                                }), d.default.ciphers[i].tagLength && !v && (v = d.default.ciphers[i].tagLength), "webCrypto" === (n = p.getCrypto()).name) {
                                if ("function" != typeof n.crypto.importKey || "function" != typeof n.crypto.encrypt) throw new Error("UnsupportedWebCrypto");
                                return [2, u.encrypt(e, a, {
                                    name: i,
                                    iv: o,
                                    additionalData: f,
                                    tagLength: v
                                }, n.crypto)]
                            }
                            if ("nodeCrypto" === n.name) return [2, l.encrypt(e, a, {
                                name: i,
                                iv: o,
                                additionalData: f,
                                tagLength: v
                            }, n.crypto)];
                            throw new Error("UnsupportedEnvironment")
                        }))
                    }))
                }
async function(e, a, n, p) {
                    e = t.decodeUTF8(e);
                    var l = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                        u = t.decodeUTF8(a),
                        d = new Uint8Array(s.randomBytes(32)),
                        m = await r.encrypt(e, d, {
                            name: "AES-GCM",
                            iv: l,
                            additionalData: u,
                            tagLength: 16
                        }),
                        f = new Uint8Array(m),
                        v = (n = new Uint8Array(Buffer.from(n, "hex")), p),
                        h = 36 + c + 16 + e.length,
                        x = new Uint8Array(h),
                        b = 0;
                    x[b] = 1, x[b += 1] = v, b += 1;
                    var g = function(e, a) {
                        var n = new Uint8Array(c + e.length),
                            t = i.box.keyPair();
                        n.set(t.publicKey);
                        var r, s, p, l = (r = t.publicKey, s = a, p = o.blake2bInit(i.box.nonceLength, null), o.blake2bUpdate(p, r), o.blake2bUpdate(p, s), o.blake2bFinal(p)),
                            u = i.box(e, l, a, t.secretKey);
                        return n.set(u, t.publicKey.length), n
                    }(d, n);
                    return x[b] = 255 & g.length, x[b + 1] = g.length >> 8 & 255, b += 2, x.set(g, b), b += 32, b += c, g.length !== 32 + c ? "encrypted key is the wrong length" : (v = (g = new Uint8Array(f)).slice(-16), g = g.slice(0, -16), x.set(v, b), b += 16, x.set(g, b), ["#PWD_BROWSER", 5, a, t.encodeBase64(x)].join(":"))
                }
