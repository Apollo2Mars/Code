        """
        use same embedding layer to represent context embedding and query embedding
        """
        layer_emb = Embedding(input_dim=self.vocab_size,
                              output_dim=self.emb_out_size,
                              weights=[self.embedding_matrix],
                              trainable=True)