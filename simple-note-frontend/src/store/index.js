import { createPinia } from 'pinia'

import useUserStore from './user'
import useNotesStore from './notes'

export default createPinia({
  useUserStore,
  useNotesStore,
});