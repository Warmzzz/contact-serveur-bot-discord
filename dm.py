
    @client.command()
    async def contact(ctx):
        first_msg = await ctx.send("Êtes-vous sure de vouloir contacter le staff ?")
        await first_msg.add_reaction("✅")
        await first_msg.add_reaction("❌")
        async def checkEmoji(reaction, user):
            return ctx.message.author == user and first_msg.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10, check=checkEmoji)
            if reaction.emoji == "✅":
                category_contact = get(guild.category_channels, id=883255892722745384)
                channel = await guild.create_text_channel(f"{ctx.message.author} | Contacte", category=category_contact)
                await channel.set_permissions(ctx.message.author, read_messages=True, send_messages=True)
                channel.send("Vous pouvez expliquer votre problème en un message :")
                def checkMessage(message):
                    return message.author == ctx.message.author and ctx.message.channel == channel
                try:
                    contact_msg = await client.wait_for("message", timeout = 600, check = checkMessage)
                except:
                    await ctx.send("Vous avez pris trop de temps, votre demande de contacte a été annulée !")
                    channel.send("Ce salon va s'auto-détruire dans 30 secondes")
                    time.sleep(30)
                    channel.delete()
                contact_channel = client.get_channel(883252300511059968)
                msg_contact_channel = await contact_channel.send(f"**__Nouvelle demande de contacte :__**\nDe **{contact_msg.author.mention}**\n\n{contact_msg}")
                contact_msg.channel.send("Votre demande de contacte a bien été envoyée !")
                contact_msg.channel.send("Ce salon va s'auto-détruire dans 30 secondes")
                time.sleep(30)
                contact_msg.channel.delete()
            elif reaction.emoji == "❌":
                await ctx.send("La demande de contacte a bien été annulée ! 1")
        except:
            await ctx.send("La demande de contacte a bien été annulée ! 2")
